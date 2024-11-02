# F4_Back
<h1 align="center">Sync Up</h1>

<p align="center">팀 프로젝트를 위해 팀원들의 성향을 분석하고 협업을 촉진하는 기능을 제공합니다.</p>

<h2>📋 개요</h2>
<p>
이 프로젝트는 팀원들의 성향을 파악하고, 협업을 촉진하기 위한 시스템을 제공합니다. 팀 구성원들이 설문을 통해 각자의 성향을 공유하고, AI를 활용해 팀의 전반적인 특성과 협업 방식을 분석하는 기능을 포함합니다.
</p>

<h2>🚀 기능</h2>
<ul>
    <li>사용자 관리 (회원가입, 로그인)</li>
    <li>설문 응답 저장 및 조회</li>
    <li>AI 기반 성향 분석 및 요약 제공</li>
    <li>팀 구성원 간의 협업 추천 사항 제공</li>
</ul>

<h2>🛠️ 기술 스택</h2>
<ul>
    <li>프레임워크: Django, Django REST Framework</li>
    <li>데이터베이스: SQLite</li>
    <li>AI API: OpenAI GPT-3.5 Turbo</li>
</ul>

<h2>📦 설치 방법</h2>

<ol>
    <li>이 저장소를 클론합니다.
        <pre><code>git clone https://github.com/moyeothon/F4_Back.git</code></pre>
    </li>
    <li>프로젝트 디렉토리로 이동합니다.
        <pre><code>cd F4_Back</code></pre>
    </li>
    <li>필요한 패키지를 설치합니다.
        <pre><code>pip install -r requirements.txt</code></pre>
    </li>
    <li>데이터베이스를 마이그레이션합니다.
        <pre><code>python manage.py migrate</code></pre>
    </li>
    <li>서버를 실행합니다.
        <pre><code>python manage.py runserver</code></pre>
    </li>
</ol>

<h2>🔑 환경 변수 설정</h2>
<p>AI API 키와 기타 환경 변수를 <code>.env</code> 파일에 설정해야 합니다.</p>
<pre><code>
OPENAI_API_KEY=your_openai_api_key
</code></pre>

<footer>
    <p align="center">Made with ❤️ by Team F4</p>
</footer>
