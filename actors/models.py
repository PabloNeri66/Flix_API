from django.db import models

# Create your models here.

NATIONALITY_CHOICES = (
    ('USA', 'Estados Unidos'),
    ('FRA', 'França'),
    ('ITA', 'Itália'),
    ('GBR', 'Reino Unido'),
    ('DEU', 'Alemanha'),
    ('IND', 'Índia'),
    ('CHN', 'China'),
    ('JPN', 'Japão'),
    ('KOR', 'Coreia do Sul'),
    ('BRA', 'Brasil'),
    ('ESP', 'Espanha'),
    ('MEX', 'México'),
    ('RUS', 'Rússia'),
    ('CAN', 'Canadá'),
    ('SWE', 'Suécia'),
    ('AUS', 'Austrália'),
    ('ARG', 'Argentina'),
    ('IRN', 'Irã'),
    ('HKG', 'Hong Kong'),
    ('EGY', 'Egito'),
)


class Actor(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nome')
    birthday = models.DateField(blank=True, null=True, verbose_name='Data de Nascimento')
    nationality = models.CharField(max_length=100, null=True, blank=True, verbose_name='Nacionalidade', choices=NATIONALITY_CHOICES)

    def __str__(self):
        return self.name
