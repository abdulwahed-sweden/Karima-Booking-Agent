import numpy as np

def calculate_compatibility(client, translator):
    weights = {
        'speed': 0.7 if client.priority == 'speed' else 0.3,
        'accuracy': 0.6,
        'cultural_fit': 0.5
    }

    scores = np.array([
        translator.speed_rating * weights['speed'],
        translator.accuracy_rating * weights['accuracy'],
        client.punctuality_rating * 0.3
    ])

    return np.mean(scores)
