def gugudan(n):
    print(n, "단을 출력합니다.")
    for i in range(1, 10):
        print(n, "x", i, "=", n*i)

# main을 통해 실행시킴
if __name__ == "__main__":
    gugudan(3)

print(__name__)