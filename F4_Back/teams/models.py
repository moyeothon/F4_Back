from django.db import models
import uuid

class Team(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    team_name = models.CharField(max_length=50, default="team")
    member_count = models.CharField(max_length=100)
    rules = models.TextField(null=True, blank=True)  # 규칙 필드
    goals = models.TextField(null=True, blank=True)  # 목표 필드

class Profile(models.Model):
    ROLE_CHOICES = [
    ('team_leader', '팀장'),
    ('team_member', '팀원'),
    ]
    PARTICIPATION_CHOICES = [
        ('frontend', '프론트엔드'),
        ('backend', '백엔드'),
        ('planning', '기획'),
        ('design', '디자인'),
    ]
    OS_CHOICES = [
        (1, 'Windows'),
        (2, 'MacOS'),
    ]
    EDITOR_MODE_CHOICES = [
        (1, '라이트 모드'),
        (2, '다크 모드'),
    ]
    WORK_ENV_CHOICES = [
        (1, '조용한 환경'),
        (2, '시끌시끌한 카페'),
    ]
    COLLAB_ENV_CHOICES = [
        (1, '오프라인 모임'),
        (2, '온라인 모임'),
    ]
    FOCUS_TIME_CHOICES = [
        (1, '아침'),
        (2, '야간'),
    ]
    PROJECT_STYLE_CHOICES = [
        (1, '계획적'),
        (2, '즉흥적'),
    ]
    COMMUNICATION_STYLE_CHOICES = [
        (1, '주기적 회의'),
        (2, '필요할 때만 연락'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='team_member')

    user_name = models.CharField(max_length=50)
    birth_date = models.DateField(null=True, blank=True)

    profile_image = models.ImageField(upload_to='profile_images/', null=True, blank=True)

    phone = models.CharField(max_length=15, null=True, blank=True)  # 전화번호 필드
    email = models.EmailField(max_length=100, null=True, blank=True)  # 이메일 필드
    github_address = models.EmailField(max_length=100, null=True, blank=True)  # GitHub 주소 필드
    # age = models.IntegerField(null=True, blank=True)
    participation_field = models.CharField(
        max_length=20,
        choices=PARTICIPATION_CHOICES
    )
    location = models.CharField(max_length=100, null=True, blank=True)  # 텍스트 입력으로 위치
    affiliations = models.CharField(max_length=100) # 소속
    mbti = models.CharField(max_length=4, null=True, blank=True)  # MBTI
    stack = models.CharField(max_length=200, null=True, blank=True)  # 기술 스택
    
    # IntegerField로 선택 필드 추가
    preferred_os = models.IntegerField(choices=OS_CHOICES)
    editor_mode = models.IntegerField(choices=EDITOR_MODE_CHOICES)
    work_environment = models.IntegerField(choices=WORK_ENV_CHOICES)
    collaboration_environment = models.IntegerField(choices=COLLAB_ENV_CHOICES)
    focus_time = models.IntegerField(choices=FOCUS_TIME_CHOICES)
    project_style = models.IntegerField(choices=PROJECT_STYLE_CHOICES)
    communication_style = models.IntegerField(choices=COMMUNICATION_STYLE_CHOICES)

    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='profiles')
    def __str__(self):
        return self.user_name