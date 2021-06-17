from django.db import models
from django.contrib.auth.models import User


class TaskModels(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)  # wbudowany system dla użytkownika,
    # foreignkey -
    # jeden uzytkownik ma wglad do wszystkiego, on_delete = co się dzieje w przypadku usuniecia konta uzytkownika,
    # w tym przypadku models.CASCADE powoduje usunięcia wszystkich danych na jego temat i wprowadzonych przez niego,
    # null - pole w db NIE MOZE BYĆ puste
    title = models.CharField(max_length=150)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)  # sprawdzanie czy jest 1 czy 0 - domyślnie jest False bo stworzony
    # nowo element nie moze być od razu ukończony
    create = models.DateTimeField(auto_now_add=True)  # automatyczne dodanie godziny po zatwierdzeniu utworzenia obiektu

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['complete']  # nieważne kiedy zwrócimy dane mają zostać uporządkowe pod complete
