

def tick(e1, e2, scores, time, report=False):
    grow_scores(e1, e2, scores)
    e1 = move(e1, scores)
    e2 = move(e2, scores)
    if report:
        print "%d: e1=%d(%s) e2=%d(%d) scores: ", scores
    return e1, e2, scores, time + 1

def move(ix, scores):
    return (ix + scores[ix] + 1) % len(scores)

def grow_scores(e1, e2, scores):
    new_score = scores[e1] + scores[e2]
    for d in str(new_score):
        scores.append(int(d))
        

    
e1 = 0
e2 = 1
scores = [3,7]
time = 0

