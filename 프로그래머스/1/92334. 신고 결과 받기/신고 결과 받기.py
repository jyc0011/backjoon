from collections import defaultdict

def solution(id_list, report, k):
    answer = [0] * len(id_list)
    reportCnt = defaultdict(set)
    mapping = {id_str: i for i, id_str in enumerate(id_list)}
    for r in set(report):
        reporter, reported = r.split()
        reportCnt[reported].add(reporter)
    for reported, reporters in reportCnt.items():
        if len(reporters) >= k:
            for reporter in reporters:
                answer[mapping[reporter]] += 1             
    return answer