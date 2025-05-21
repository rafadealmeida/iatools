from django.db import models
from datetime import datetime

class IATool(models.Model):
    
    OPCOES_CATEGORIA = [
        ("GPT", "gpt"),
        ("VIDEOS", "vídeos"),
        ("IMAGENS", "imagens"),
        ("AUDIOS", "áudios")
    ]

    nome = models.CharField(max_length=100, null=False, blank=False)
    legenda = models.CharField(max_length=150, null=False, blank=False)
    categoria = models.CharField(
        max_length=100,
        choices=OPCOES_CATEGORIA,
        default=''
    )
    descricao = models.TextField(null=False, blank=False)
    icone = models.ImageField(
        upload_to="iatools/icones/%Y/%m/%d/",
        blank=True
    )
    publicada = models.BooleanField(default=False)
    data_publicacao = models.DateTimeField(default=datetime.now, blank=False)

    def __str__(self):
        return f"IATool [nome={self.nome}]"
