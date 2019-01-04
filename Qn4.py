from random import randint
from functools import reduce

name_list = [
  'Ada',
  'Bala',
  'Chloe',
  'Dylan',
  'Elvin',
  'Fadhilah',
  'Gwendolyn',
  'Hakim',
  'Ian',
  'Jeremy'
]

def get_medal(score):
  if score >= 80:
    return 'Gold'
  elif score >= 60 and score <= 79:
    return 'Silver'
  elif score >= 49 and score <= 59:
    return 'Bronze'
  else:
    return None

preliminary_queue = []

for idx, name in enumerate(name_list):
  score1  = randint(0, 100)
  preliminary_queue.insert(0, {'name': name, 'score1': score1})
  print('Participant #{}: {} - {}'.format(idx+1, name, score1))

print('\n')
print('Final round starts...\n')

finalQ = [{'name': participant['name'], 'score2': randint(0, 100)} for participant in preliminary_queue if participant['score1'] >= 50]

for idx, participant in enumerate(finalQ):
  str = 'Participant #{}: {} - {}'.format(idx+1, participant['name'], participant['score2'])
  medal = get_medal(participant['score2'])
  if medal != None:
    str += ' - {}'.format(medal)
  print(str)

prelim_avg_score = reduce(lambda total, score: total + score, [participant['score1'] for participant in preliminary_queue]) / len(preliminary_queue)
percentage = len(finalQ) / len(preliminary_queue) * 100
num_medals = len([participant for participant in finalQ if get_medal(participant['score2']) != None])

print('\n')
print('The average/mean score for preliminary round is {:.1f}.\n'.format(prelim_avg_score))
print('The percentage of participants getting into final round is {:.1f}.\n'.format(percentage))
print('The number of participants getting a medal is {}.'.format(num_medals))