// 두 단어 비교
func calc(word1, word2 string) bool { // 매개변수 둘 다 string, 리턴 bool 
	diffCount := 0 // 비교 카운터 초기 값 0
	for i := range word1 { // word1을 순회하면서
		if word1[i] != word2[i] { // 같은 게 있다면
			diffCount++ // 카운터 증가
		}
		if diffCount > 1 { // 두 개 이상 다르면
			return false // false를 반환
		}
	}
	return diffCount == 1 // 한 글자만 다르면 true를 반환
}

func solution(begin string, target string, words []string) int {
	wordMap := make(map[string]bool) // 맵 생성
	for _, word := range words {
		wordMap[word] = true // 리스트를 맵으로 변환 
	}

	if !wordMap[target] {
		return 0 // target 없음 -> 변환 X
	}

	queue := []struct {	// 큐 초기화 (구조체 생성)
		word  string
		idx int
	}{ {word: begin, idx: 0} }
	visited := make(map[string]bool)
	visited[begin] = true // 시작 단어 -> 방문 처리

	// BFS
	for len(queue) > 0 { // 큐가 빌 때까지
		current := queue[0] // 하나 꺼내고
		queue = queue[1:] // 슬라이싱
		if current.word == target {// target 단어 도달
			return current.idx // 현재 인덱스 반환
		}

		for word := range wordMap { // 단어 검사
			if !visited[word] && calc(current.word, word) { // 방문 안 함 & 한 글자만 다름
				visited[word] = true // 방문 처리
				queue = append(queue, struct{word string; idx int}{word, current.idx + 1}) 
			} // 큐에 추가
		}
	}
	return 0
}