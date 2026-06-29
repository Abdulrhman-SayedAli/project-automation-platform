import asyncio
import signal

from app.core.config import get_settings
from app.core.logging import configure_logging, get_logger


async def run() -> None:
    settings = get_settings()
    configure_logging(settings.log_level)
    logger = get_logger(__name__)
    stop_event = asyncio.Event()

    def request_stop() -> None:
        stop_event.set()

    loop = asyncio.get_running_loop()
    for sig in (signal.SIGINT, signal.SIGTERM):
        try:
            loop.add_signal_handler(sig, request_stop)
        except NotImplementedError:
            signal.signal(sig, lambda _signum, _frame: request_stop())

    logger.info(
        "worker_container_ready",
        event_type="worker_container_ready",
        worker_count=settings.worker_count,
        provider=settings.coding_provider,
    )
    await stop_event.wait()
    logger.info("worker_container_stopping", event_type="worker_container_stopping")


def main() -> None:
    asyncio.run(run())


if __name__ == "__main__":
    main()

