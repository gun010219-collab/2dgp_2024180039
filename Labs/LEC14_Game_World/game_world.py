#world = [] 1차원 리스트
world = [ [], [], [] ] #0번 1번 2번 레이어

# 게임 월드에 객체 추가, 레이어를 지정해야한다
def add_object(o, depth):
    world[depth].append(o)

# 게임 월드에서 객체 제거
def remove_object(o):
    for layer in world:
        if o in layer:
            layer.remove(o)
            return # 더이상 찾을 필요가 없으므로 return으로 종료


#game logic
def update():
    for layer in world:
        for o in layer:
            o.update()

#game randering
def rander():
    for layer in world:
        for o in layer:
            o.draw()