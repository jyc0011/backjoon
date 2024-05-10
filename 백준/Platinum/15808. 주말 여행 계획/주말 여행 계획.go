package main

import (
	"bufio"
	"container/heap"
	"fmt"
	"os"
	"strconv"
	"strings"
)

const INFINITY = 1<<31 - 1

type Edge struct {
	to, cost int
}

type PriorityQueue []*Vertex
type Vertex struct {
	id, dist int
	index    int
}

func (pq PriorityQueue) Len() int           { return len(pq) }
func (pq PriorityQueue) Less(i, j int) bool { return pq[i].dist < pq[j].dist }
func (pq PriorityQueue) Swap(i, j int) {
	pq[i], pq[j] = pq[j], pq[i]
	pq[i].index = i
	pq[j].index = j
}
func (pq *PriorityQueue) Push(x interface{}) {
	n := len(*pq)
	item := x.(*Vertex)
	item.index = n
	*pq = append(*pq, item)
}
func (pq *PriorityQueue) Pop() interface{} {
	old := *pq
	n := len(old)
	item := old[n-1]
	old[n-1] = nil // avoid memory leak
	item.index = -1
	*pq = old[0 : n-1]
	return item
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Split(bufio.ScanLines)
	scanner.Buffer(make([]byte, 1024*1024), 10*1024*1024)

	scanner.Scan()
	n, _ := strconv.Atoi(scanner.Text())
	adj := make([][]Edge, n)

	for i := 0; i < n; i++ {
		scanner.Scan()
		weights := strings.Fields(scanner.Text())
		for j, w := range weights {
			cost, _ := strconv.Atoi(w)
			if cost != 0 {
				adj[i] = append(adj[i], Edge{j, cost})
			}
		}
	}

	scanner.Scan()
	params := strings.Fields(scanner.Text())
	p, _ := strconv.Atoi(params[0])
	q, _ := strconv.Atoi(params[1])

	dist := make([]int, n)
	for i := range dist {
		dist[i] = INFINITY
	}

	pq := &PriorityQueue{}
	heap.Init(pq)

	for i := 0; i < p; i++ {
		scanner.Scan()
		tour := strings.Fields(scanner.Text())
		lj, _ := strconv.Atoi(tour[0])
		wj, _ := strconv.Atoi(tour[1])
		lj-- // Convert to zero-indexed
		dist[lj] = -wj
		heap.Push(pq, &Vertex{id: lj, dist: dist[lj]})
	}

	hotels := make([]int, n)
	for i := 0; i < q; i++ {
		scanner.Scan()
		hotel := strings.Fields(scanner.Text())
		li, _ := strconv.Atoi(hotel[0])
		wi, _ := strconv.Atoi(hotel[1])
		li-- // Convert to zero-indexed
		hotels[li] = wi
	}

	for pq.Len() > 0 {
		curr := heap.Pop(pq).(*Vertex)
		if dist[curr.id] < curr.dist {
			continue
		}
		for _, edge := range adj[curr.id] {
			newDist := curr.dist + edge.cost
			if newDist < dist[edge.to] {
				dist[edge.to] = newDist
				heap.Push(pq, &Vertex{id: edge.to, dist: newDist})
			}
		}
	}

	maxValue := -INFINITY
	for i, hotelCost := range hotels {
		if hotelCost != 0 && dist[i] != INFINITY {
			maxValue = max(maxValue, hotelCost-dist[i])
		}
	}

	fmt.Println(maxValue)
}

func max(x, y int) int {
	if x > y {
		return x
	}
	return y
}