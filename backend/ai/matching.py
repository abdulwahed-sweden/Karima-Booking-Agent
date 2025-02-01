import numpy as np

def calculate_compatibility(client, translator):
    """
    تحسب درجة التوافق بين العميل والمترجم بناءً على عوامل مثل:
    - السرعة
    - الدقة
    - الالتزام بالمواعيد
    """
    # الأوزان لتفضيلات العميل
    weights = {
        'speed': 0.7 if client.get('priority') == 'speed' else 0.3,
        'accuracy': 0.6,
        'cultural_fit': 0.5
    }

    # حساب درجة التوافق
    scores = np.array([
        translator.get('speed_rating', 0) * weights['speed'],          # تقييم السرعة
        translator.get('accuracy_rating', 0) * weights['accuracy'],   # تقييم الدقة
        client.get('punctuality_rating', 0) * 0.3                     # تقييم الالتزام بالمواعيد
    ])

    # المتوسط كدرجة التوافق النهائية
    return np.mean(scores)


def match_translators(client_profile, translators):
    """
    مطابقة العميل مع قائمة من المترجمين بناءً على التوافق.
    """
    results = []

    # حساب التوافق لكل مترجم
    for translator in translators:
        score = calculate_compatibility(client_profile, translator)
        results.append({
            'translator': translator,
            'score': round(score, 2)  # تقليل الدقة إلى منزلتين عشريتين
        })

    # ترتيب النتائج بناءً على درجة التوافق
    results = sorted(results, key=lambda x: x['score'], reverse=True)

    return results[:3]  # إعادة أفضل 3 مترجمين فقط
