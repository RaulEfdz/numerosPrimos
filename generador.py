from collections import Counter
import random
limit = 100000000000
print('Longitud meta:', len(str(limit)))
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_sequence(gaps):
    sequence = [2]  # Comenzamos con 2, el primer número primo
    for gap in gaps:
        sequence.append(sequence[-1] + gap)
    return sequence

def predict_next(sequence, k=3):
    counter = Counter(sequence)
    total = len(sequence)
    numbers, probabilities = zip(*[(num, count/total) for num, count in counter.items()])
    prediction = random.sample(numbers, k)
    prediction_probabilities = [probabilities[numbers.index(num)] for num in prediction]
    additional_predictions = random.sample(prediction, 2)
    prediction.extend(additional_predictions)
    prediction_probabilities.extend([probabilities[numbers.index(num)] for num in additional_predictions])
    max_additional_prediction = max(additional_predictions)
    random_number = random.randint(max_additional_prediction + 1, max_additional_prediction * 2)
    prediction.append(random_number)
    prediction_probabilities.append(0)
    return list(zip(prediction, prediction_probabilities))
