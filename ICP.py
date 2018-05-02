def odom_abs_to_rel(origin_rot, origin_pos, rot, pos):
    return origin_rot.T @ rot, origin_rot.T @ (
                pos - origin_pos)  # @ is matrix multiplication operator since Python 3.5. If you have lower Python, use np.matmul(a, b)


def odom_rel_to_abs(origin_rot, origin_pos, rel_rot, rel_pos):
    return origin_rot @ rel_rot, origin_rot @ rel_pos + origin_pos


def reject(p, q):
    """
    reject worst 20% of pairs, based on point to point distance
    """
    # array of distances
    dists = [(np.linalg.norm(p[i] - q[i]), i) for i in range(len(p))]
    # sort based on distance, largest first
    dists.sort(key=lambda x: x[0], reverse=True)

    num_remove = int(.3 * len(q))

    dists = dists[:num_remove]

    for _, i in sorted(dists, key=lambda x: x[1], reverse=True):
        q = delete(q, i, 0)
        p = delete(p, i, 0)
    return p, q


def random_indexes(p, number_of_samples):
    _, n = p.shape
    indexes = np.arange(0, n)
    indexes = rd.sample(list(indexes), number_of_samples)
    samples = np.zeros((2, len(indexes)))
    for i in range(0, len(indexes)):
        samples[:, i] = p[:, indexes[i]]

    return samples


def icp(pointcloud, new_pts, init_rot=None, init_trans=None, max_tolerance=0.001, max_iters=None, outlier_ratio=0.0,
        verbose=True):
    R = init_rot
    T = init_trans

    # filter data
    q = pointcloud[:, ~np.isnan(pointcloud[0, :])]
    p = new_pts[:, ~np.isnan(new_pts[0, :])]
    backup_new = p

    # Initial transformation
    p = np.add(p, T)
    p = R.dot(p)

    Tres = T
    Rres = R
    Trel = np.zeros((2, 1))
    Rrel = np.identity(2)

    # use Kd tree to find relations between points
    tree = spatial.KDTree(q.T)

    err = 1
    cnt = 0
    while cnt < 30:
        cnt = cnt + 1
        number_of_samples = 100

        p_sam = random_indexes(p, number_of_samples)
        nbs, ind = tree.query(p_sam.T)
        q_sam = q[:, ind]

        p_sam, q_sam = reject(p_sam, q_sam)

        # print(p_sam.shape)
        # print(q_sam.shape)

        phat = p_sam.mean(axis=1)
        qhat = q_sam.mean(axis=1)

        T = qhat - phat
        T = np.array([[T[0]], [T[1]]])
        Tres = np.add(Tres, T)
        Trel = np.add(Trel, T)
        # print(T)

        # fig = plt.figure(frameon=True)
        # ax = fig.gca()
        # ax.axis('equal')
        # ax.invert_xaxis()

        # p_sam = np.add(p_sam,T)
        # phat = p_sam.mean(axis=1)

        # print(samples[:,:].T)
        err = sum(phat - qhat)

        p_centered = np.add(p_sam[:, :], T)
        q_centered = q_sam

        # print(p_centered.shape)
        # print(q_centered.shape)
        # ax.scatter(p[1, :], p[0, :], c='b')
        # ax.scatter(p_sam[1, :], p_sam[0, :], c='r')
        # ax.scatter((p_centered)[1, :], (p_centered)[0, :], c='g')
        # ax.scatter(phat[1], phat[0], c='g')
        # ax.scatter(q[1, :], q[0, :], c='y')
        # ax.scatter(q_sam[1, :], q_sam[0, :], c='r')
        # ax.scatter((q_centered)[1, :], (q_centered)[0, :], c='b')
        # ax.scatter(qhat[1], qhat[0], c='b')
        # print(q_centered[:,:].T)

        # print("H")
        H = ((p_centered)[:, :]).dot((q_centered.T[:, :]))

        U, s, V = np.linalg.svd(H, full_matrices=True)
        R = (V.T).dot(U.T)
        Rres = Rres.dot(R)
        Rrel = Rres.dot(R)

        p = np.add(p, T)
        p = R.dot(p)

    # print(Rres)
    # print(Tres)

    return Rres, Tres, Rrel, Trel