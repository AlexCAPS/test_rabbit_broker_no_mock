import pytest

from faststream.rabbit import RabbitBroker, TestRabbitBroker
broker = RabbitBroker()

@pytest.mark.asyncio
async def test_handle():
    async with TestRabbitBroker(broker) as br:
        await br.publish('', queue='test-queue')
        await br.request('', queue='test-queue')    # raise faststream.exceptions.SubscriberNotFound