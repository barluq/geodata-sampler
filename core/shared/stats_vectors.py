from dataclasses import dataclass
from core.shared.models_vectors import VectorEntity, VectorEntityFeature


@dataclass
class VectorEntityStats():
    features_count: int
    properties_per_feature_count: int

    @staticmethod
    def from_vector_entity(vector_entity: VectorEntity) -> "VectorEntityStats":
        """
        Creates a VectorEntityStats instance from a VectorEntity.

        Args:
            vector_entity (VectorEntity): The vector entity to extract statistics from.

        Returns:
            VectorEntityStats: An instance containing statistics derived from the vector entity.
        """

        def count_properties(feature: VectorEntityFeature) -> int:
            return len(feature.properties)
        
        features_count = len(vector_entity.features)
        properties_per_feature_count = count_properties(vector_entity.features[0]) if vector_entity.features else 0

        return VectorEntityStats(
            features_count=features_count,
            properties_per_feature_count=properties_per_feature_count,
        )