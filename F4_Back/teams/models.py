from django.db import models
from django.contrib.auth.models import User
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
    preferred_os = models.IntegerField(choices=OS_CHOICES, default=1 )
    editor_mode = models.IntegerField(choices=EDITOR_MODE_CHOICES, default=1)
    work_environment = models.IntegerField(choices=WORK_ENV_CHOICES, default=1)
    collaboration_environment = models.IntegerField(choices=COLLAB_ENV_CHOICES, default=1)
    focus_time = models.IntegerField(choices=FOCUS_TIME_CHOICES, default=1)
    project_style = models.IntegerField(choices=PROJECT_STYLE_CHOICES, default=1)
    communication_style = models.IntegerField(choices=COMMUNICATION_STYLE_CHOICES, default=1)

    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='profiles')
    def __str__(self):
        return self.user_name
    
class ProfileQuestionAnswer(models.Model):
    QUESTION_CHOICES = [
        (1, '이번 팀 프로젝트에서 가장 챙겨가고 싶은 점은 무엇인가요?'),
        (2, '가장 중요하게 생각하는 협업 요소는 무엇인가요?'),
        (3, '팀원들과의 관계에서 가장 중요하게 생각하는 점은 무엇인가요?'),
        (4, '프로젝트가 끝난 후 팀원들에게 어떤 모습으로 기억되고 싶은가요?'),
        (5, '프로젝트를 진행하면서 스스로에게 가장 엄격하게 적용하고 싶은 원칙은 무엇인가요?')
    ]

    ANSWER_CHOICES = {
        1: [
            (1, '팀원들과의 네트워킹'),
            (2, '새로운 개발 기술 도전'),
            (3, '팀원들과의 협업 경험'),
            (4, '문제 해결 능력 강화')
        ],
        2: [
            (1, '명확한 목표와 방향 설정'),
            (2, '팀원들 간의 신뢰와 존중'),
            (3, '일정과 마감 기한 준수'),
            (4, '자발적이고 적극적인 참여')
        ],
        3: [
            (1, '신뢰와 존중'),
            (2, '서로의 역할에 대한 이해와 존중'),
            (3, '친밀한 관계와 팀워크'),
            (4, '자유로운 의견 교환과 소통')
        ],
        4: [
            (1, '항상 문제를 해결하려고 노력했던 사람'),
            (2, '팀 분위기를 밝게 만들고 소통을 원할하게 했던 사람'),
            (3, '신뢰할 수 있고 책임감 있게 맡은 일을 수행했던 사람'),
            (4, '새로운 아이디어와 관점으로 프로젝트에 기여했던 사람')
        ],
        5: [
            (1, '맡은 일에 끝까지 책임지는 자세'),
            (2, '팀원들의 의견을 존중하고 경청하는 태도'),
            (3, '정해진 일정과 마감을 철저히 지키는 시간 관리'),
            (4, '문제에 직면했을 때 포기하지 않고 끝까지 해결하려는 의지')
        ]
    }

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='question_answers')
    team = models.ForeignKey(Team, on_delete=models.CASCADE)  # team 필드 추가
    question_id = models.IntegerField(choices=QUESTION_CHOICES)  # 질문 선택
    answer_id = models.IntegerField()  # 답변 선택

    def __str__(self):
        return f"Profile {self.profile.id} - Question {self.question_id}"

    def get_answer_display(self):
        return dict(self.ANSWER_CHOICES[self.question_id])[self.answer_id]