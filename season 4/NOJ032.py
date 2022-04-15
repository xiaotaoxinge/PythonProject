nums = input().split(' ')
target = input()
try:
    print(nums.index(target))
except Exception:
    print(-1)