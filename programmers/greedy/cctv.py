def solution(routes):
    # ascending sort with start pos
    routes.sort()
    answer = 0 # the number of camera
    cam = [] # current camera coverage
    for idx in range(len(routes)):
        if not cam:
            cam = routes[idx]
            answer += 1
        else:
            if cam[1] >= routes[idx][0]:
                cam = [routes[idx][0], min(cam[1], routes[idx][1])]
            else:
                answer += 1
                cam = routes[idx]
    return answer

routes = [[-20,-15], [-14,-5], [-18,-13], [-5,-3]]
print(solution(routes)) # 2
routes = [[-20,-10], [-5,5], [-15,0]]
print(solution(routes)) # 2