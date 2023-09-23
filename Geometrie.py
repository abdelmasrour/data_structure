import math
def circle_city(raduis: int,k :int )-> str:
    list_y = [i**2 for i in range(1,raduis)]
    s_integer= 4 # counter des entiers touche la cercle 
    s_inside=0
    for x in range(1,math.ceil(raduis/2)+1):
        print(raduis**2-x**2)
        print(x)
        if raduis**2-x**2 in list_y:
            s_inside += 1
    print(s_integer + 8*s_inside)
    if s_integer + 8*s_inside==k:
        return "possible"
    return "impossible"

if __name__=="__main__" : 
    k = 4
    raduis = 5
    print(f'{circle_city(5,4)} circle_city of raduis{raduis} and k{k} policiers')
