# Generated by Django 4.2.12 on 2024-10-06 20:40

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('surname', models.CharField(blank=True, max_length=255, verbose_name='Фамилия')),
                ('given_name', models.CharField(blank=True, max_length=255, verbose_name='Имя')),
                ('patronymic', models.CharField(blank=True, max_length=255, verbose_name='Отчество')),
                ('group_number', models.CharField(blank=True, max_length=50, verbose_name='Номер группы')),
                ('date_of_birth', models.DateField(blank=True, null=True, verbose_name='Дата рождения')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Название курса')),
                ('description', models.TextField(verbose_name='Описание')),
                ('instructor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courses', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CourseMaterialPreference',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Название предпочтения')),
            ],
            options={
                'verbose_name': 'Предпочтение учебного материала',
                'verbose_name_plural': 'Предпочтения учебных материалов',
            },
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название теста')),
            ],
            options={
                'verbose_name': 'Тест',
                'verbose_name_plural': 'Тесты',
            },
        ),
        migrations.CreateModel(
            name='TestItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_type', models.CharField(choices=[('single_choice', 'Один вариант'), ('multiple_choice', 'Несколько вариантов'), ('text', 'Текстовый ответ')], max_length=50, verbose_name='Тип вопроса')),
                ('content', models.TextField(verbose_name='Вопрос')),
                ('correct_text_answer', models.TextField(blank=True, null=True, verbose_name='Правильный текстовый ответ')),
                ('order_index', models.PositiveIntegerField(default=0, verbose_name='Порядок отображения')),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='learnsys.test', verbose_name='Тест')),
            ],
            options={
                'verbose_name': 'Вопрос теста',
                'verbose_name_plural': 'Вопросы тестов',
                'ordering': ['order_index'],
            },
        ),
        migrations.CreateModel(
            name='TestItemOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=255, verbose_name='Вариант ответа')),
                ('is_correct', models.BooleanField(default=False, verbose_name='Правильный ответ')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='options', to='learnsys.testitem', verbose_name='Вопрос')),
            ],
            options={
                'verbose_name': 'Вариант ответа',
                'verbose_name_plural': 'Варианты ответов',
            },
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название темы')),
                ('description', models.TextField(verbose_name='Описание')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='topics', to='learnsys.course', verbose_name='Курс')),
                ('parent_topic', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subtopics', to='learnsys.topic', verbose_name='Родительская тема')),
            ],
            options={
                'verbose_name': 'Тема',
                'verbose_name_plural': 'Темы',
            },
        ),
        migrations.CreateModel(
            name='UserTestAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_answer', models.TextField(blank=True, verbose_name='Текстовый ответ')),
                ('date_answered', models.DateTimeField(auto_now_add=True, verbose_name='Дата ответа')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='learnsys.testitem', verbose_name='Вопрос')),
                ('option', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='learnsys.testitemoption', verbose_name='Выбранный вариант')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Ответ пользователя',
                'verbose_name_plural': 'Ответы пользователей',
            },
        ),
        migrations.CreateModel(
            name='TopicContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_type', models.CharField(choices=[('text', 'Текст'), ('file', 'Файл'), ('image', 'Изображение'), ('video', 'Видео'), ('audio', 'Аудио')], max_length=50, verbose_name='Тип контента')),
                ('content', models.FileField(blank=True, null=True, upload_to='topic_contents/', verbose_name='Файл')),
                ('text_content', models.TextField(blank=True, null=True, verbose_name='Текстовое содержимое')),
                ('order_index', models.PositiveIntegerField(default=0, verbose_name='Порядок отображения')),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contents', to='learnsys.topic')),
            ],
            options={
                'verbose_name': 'Материал темы',
                'verbose_name_plural': 'Материалы тем',
            },
        ),
        migrations.AddField(
            model_name='test',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tests', to='learnsys.topic', verbose_name='Тема'),
        ),
        migrations.CreateModel(
            name='StudyGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('courses', models.ManyToManyField(blank=True, related_name='study_groups', to='learnsys.course', verbose_name='Курсы')),
            ],
        ),
        migrations.CreateModel(
            name='TestResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(default=0, verbose_name='Количество правильных ответов')),
                ('total_questions', models.IntegerField(default=0, verbose_name='Общее количество вопросов в тесте')),
                ('date_taken', models.DateTimeField(auto_now_add=True, verbose_name='Дата прохождения')),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='test_results', to='learnsys.test', verbose_name='Тест')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Результат теста',
                'verbose_name_plural': 'Результаты тестов',
                'unique_together': {('user', 'test')},
            },
        ),
        migrations.CreateModel(
            name='PsychologicalTestResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('preference', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='learnsys.coursematerialpreference', verbose_name='Предпочтение')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Результат психологического теста',
                'verbose_name_plural': 'Результаты психологических тестов',
                'unique_together': {('user', 'preference')},
            },
        ),
        migrations.CreateModel(
            name='GroupMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('study_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='group_members', to='learnsys.studygroup', verbose_name='Учебная группа')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_group_memberships', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Участник учебной группы',
                'verbose_name_plural': 'Участники учебных групп',
                'unique_together': {('study_group', 'user')},
            },
        ),
    ]