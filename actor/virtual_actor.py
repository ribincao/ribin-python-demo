import time

class VirtualActor:
    def __init__(self, actor_id, num_shards=3):
        self.actor_id = actor_id
        self.num_shards = num_shards
        self.shards = {}

    def get_shard_id(self, key):
        return hash(key) % self.num_shards

    def get_shard(self, key):
        shard_id = self.get_shard_id(key)
        if shard_id not in self.shards:
            self.shards[shard_id] = {}
        return self.shards[shard_id]

    def set(self, key, value):
        shard = self.get_shard(key)
        shard[key] = value

    def get(self, key):
        shard = self.get_shard(key)
        return shard.get(key)

def process_message(actor_id, message):
    # 将消息转发到虚拟 Actor 对象中
    actor.set(message['key'], message['value'])

# 创建一个虚拟 Actor
actor = VirtualActor('test_actor')

# 模拟接收到一些消息
messages = [
    {'key': 'key1', 'value': 'value1'},
    {'key': 'key2', 'value': 'value2'},
    {'key': 'key3', 'value': 'value3'},
]

for message in messages:
    process_message(actor.actor_id, message)

# 等待一段时间
time.sleep(1)

# 打印虚拟 Actor 中保存的状态
print(actor.shards)

