from dataclasses import dataclass
from enum import StrEnum


class SourceType(StrEnum):
    GOOGLE_RESEARCH = "google_research"
    INSTAGRAM = "instagram"
    FACEBOOK = "facebook"
    WEB = "web"
    CURATED = "curated"


@dataclass(frozen=True)
class SourcePacket:
    title: str
    content: str
    source: str


class ConnectorRegistry:
    """Safe connector abstraction for demos and future OAuth/API integrations.

    The hackathon demo uses curated public-domain style snippets instead of scraping social
    platforms. Production connectors should use each platform's official API, OAuth consent,
    rate limits, and terms-compliant data access.
    """

    def collect(self, topic: str, sources: list[SourceType] | None = None) -> list[SourcePacket]:
        selected = sources or [SourceType.GOOGLE_RESEARCH, SourceType.CURATED]
        packets: list[SourcePacket] = []
        for source in selected:
            packets.append(self._demo_packet(topic, source))
        return packets

    def _demo_packet(self, topic: str, source: SourceType) -> SourcePacket:
        topic_label = topic.strip() or "general science"
        content = (
            f"Research notes about {topic_label}. Newton's second law states that force equals "
            "mass times acceleration, often written as F = m a. Gravity is an attractive "
            "interaction between masses and causes objects near Earth to accelerate downward. "
            "A reliable learning system should retrieve evidence before answering, compare the "
            "answer against the evidence, and correct unsupported claims."
        )
        return SourcePacket(title=f"{source.value}: {topic_label}", content=content, source=source.value)
