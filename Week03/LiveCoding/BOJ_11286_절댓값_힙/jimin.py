import heapq
import sys
N=int(sys.stdin.readline())

heap=[]
mheap=[]

for _ in range(N):
    x=int(sys.stdin.readline())

    if x!=0:
        if x>0:
            heapq.heappush(heap, x)
        else:
            heapq.heappush(mheap,-x)
    else:
        if len(heap) ==0 and len(mheap)==0:
            print(0)
        elif len(heap)==0:
            print(-heapq.heappop(mheap))
        elif len(mheap)==0:
            print(heapq.heappop(heap))
        else:
            if mheap[0] <= heap[0]:
                print(-heapq.heappop(mheap))
            else:
                print(heapq.heappop(heap))