import random
import uuid
import datetime
from collections import defaultdict, Counter

import lorem



messages = [
    {
        "id": "efadb781-9b04-4aad-9afe-e79faef8cffb",
        "sent_at": datetime.datetime(2022, 10, 11, 23, 11, 11, 721),
        "sent_by": 46,  # id пользователя-отправителя
        "reply_for": "7b22ae19-6c58-443e-b138-e22784878581",  # id сообщение, на которое это сообщение является ответом (может быть None)
        "seen_by": [26, 91, 71], # идентификаторы пользователей, которые видели это сообщение
        "text": "А когда ревью будет?",
    }
]


def generate_chat_history():
    messages_amount = random.randint(200, 1000)
    users_ids = list(
        {random.randint(1, 10000) for _ in range(random.randint(5, 20))}
    )
    sent_at = datetime.datetime.now() - datetime.timedelta(days=100)
    messages = []
    for _ in range(messages_amount):
        sent_at += datetime.timedelta(minutes=random.randint(0, 240))
        messages.append({
            "id": uuid.uuid4(),
            "sent_at": sent_at,
            "sent_by": random.choice(users_ids),
            "reply_for": random.choice(
                [
                    None,
                    (
                        random.choice([m["id"] for m in messages])
                        if messages else None
                    ),
                ],
            ),
            "seen_by": random.sample(users_ids,
                                     random.randint(1, len(users_ids))),
            "text": lorem.sentence(),
        })
    return messages


def find_most_active_user(messages):
    user_message_count = Counter(message['sent_by'] for message in messages)
    most_active_user = user_message_count.most_common(1)[0][0]
    return most_active_user


def find_most_replied_user(messages):
    reply_count = Counter(message['reply_for'] for message in messages if message['reply_for'])
    most_replied_message = reply_count.most_common(1)[0][0]
    most_replied_user = next(message['sent_by'] for message in messages if message['id'] == most_replied_message)
    return most_replied_user


def find_most_seen_users(messages):
    seen_by_count = defaultdict(set)
    for message in messages:
        seen_by_count[message['sent_by']].update(message['seen_by'])
    most_seen_users = sorted(seen_by_count, key=lambda user: len(seen_by_count[user]), reverse=True)[:5]
    return most_seen_users


def find_most_active_period(messages):
    time_period_count = defaultdict(int)
    for message in messages:
        hour = message['sent_at'].hour
        if hour < 12:
            time_period_count['morning'] += 1
        elif 12 <= hour < 18:
            time_period_count['afternoon'] += 1
        else:
            time_period_count['evening'] += 1
    most_active_period = max(time_period_count, key=time_period_count.get)
    return most_active_period


def find_longest_threads(messages):
    thread_length = defaultdict(int)
    for message in messages:
        if message['reply_for']:
            thread_length[message['reply_for']] += 1
    longest_threads = sorted(thread_length, key=thread_length.get, reverse=True)[:5]
    return longest_threads


if __name__ == "__main__":
    messages = generate_chat_history()

    most_active_user = find_most_active_user(messages)
    print(f"Айди пользователя, который написал больше всех сообщений: {most_active_user}")

    most_replied_user = find_most_replied_user(messages)
    print(f"Айди пользователя, на сообщения которого больше всего отвечали: {most_replied_user}")

    most_seen_users = find_most_seen_users(messages)
    print(f"Айди пользователей, сообщения которых видело больше всего уникальных пользователей: {most_seen_users}")

    most_active_period = find_most_active_period(messages)
    print(f"Больше всего сообщений в чате: {most_active_period}")

    longest_threads = find_longest_threads(messages)
    print(f"Идентификаторы сообщений, которые стали началом для самых длинных тредов: {longest_threads}")