def solution(H):
    blocks = 0
    stack = []
    for i in range(len(H)):
        
        j = len(stack) - 1
        while j >= 0 and stack[j] > H[i]:
            stack.pop()
            j -= 1

        if not stack or stack[j] != H[i]:
            stack.append(H[i])
            blocks += 1

    return blocks