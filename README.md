# Demo app for learning django

**Added Vector Similarity Search using pgVector**

```python
# in models file
from pgvector.django import HnswIndex

class File(models.Model):
    # ... other fields ...
    
    class Meta:
        indexes = [
            HnswIndex(
                name="clip_l14_vectors_index",
                fields=["embedding_clip_vit_l_14"],
                m=16,
                ef_construction=64,
                opclasses=["vector_cosine_ops"],
            )
        ]
        
# In  application
from pgvector.django import CosineDistance

def search_image_embedding(self, embedding):
    user_files = File.objects.filter(connector__user=self.user)
    
    files_with_distance = user_files.annotate(
        distance=CosineDistance("embedding_clip_vit_l_14", embedding)
    ).order_by("distance")[:12]
    
    # Processing and return the search results
    # Check the repo
```