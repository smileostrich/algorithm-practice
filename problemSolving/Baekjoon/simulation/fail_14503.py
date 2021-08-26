# # 20.10.27 time fail
#
# from sys import stdin
#
# inp = lambda: map(int, stdin.readline().split())
#
# #입력
# mat_x, mat_y = inp()
# robot_loc_r, robot_loc_c, robot_face = inp()
#
# matrix = []
# for _ in range(mat_x):
#     matrix.append(list(inp()))
#
#
# # def clean(x, y):
# #     if matrix[x][y] == 0:
# #
# #         return 0
# #     else:
# #         matrix[x][y] = 0
# #         return 1
#
#
# def update_face(face):
#     if face == 0:
#         return 3
#     else:
#         return face-1
#
#
# def check_left(x, y, robot_face):
#     if matrix[x][y] == 0:
#         move()
#         # return x, y, update_face(robot_face)
#     else:
#         return x, y, update_face(robot_face)
#
#
# def move(x, y, robot_face):
#     global clean_cnt
#     global matrix
#     clean_cnt += 1
#     matrix[x][y] = 2
#
#
# def move_back(x, y, robot_face):
#     global clean_cnt
#     global matrix
#     clean_cnt += 1
#     matrix[x][y] = 2
#
#
# def check_back(x, y, robot_face):
#     if robot_face == 0:
#         if matrix[x+1][y] == 0:
#             return x+1, y
#         else:
#             return -1
#     elif robot_face == 1:
#         if matrix[x][y-1] == 0:
#             return x, y-1
#         else:
#             return -1
#     elif robot_face == 2:
#         if matrix[x-1][y] == 0:
#             return x-1, y
#         else:
#             return -1
#     elif robot_face == 3:
#         if matrix[x][y+1] == 0:
#             return x, y+1
#         else:
#             return -1
#
#
# def check_four(x, y, robot_face, rotate_cnt):
#     if check_left() ==
#     rotate_cnt += 1
#     return -1
#
#
#
# def search(x,y,robot_face):
#     rotate_cnt = 0
#     while True:
#         if rotate_cnt != 4:
#             x, y, robot_face = check_left()
#             rotate_cnt += 1
#         else:
#             if check_back(x, y, robot_face) == -1:
#                 print(clean_cnt)
#                 break
#
# # config
# clean_cnt = 0
#
#
# # 시작
# clean_cnt += 1
# matrix[robot_loc_r][robot_loc_c] = 2
#
# search(robot_loc_r, robot_loc_c, robot_face)
# if rotate_cnt =
#
#
