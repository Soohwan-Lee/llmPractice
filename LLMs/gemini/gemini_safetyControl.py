# https://wikidocs.net/229822
import google.generativeai as genai
import os

# genai.configure(api_key=os.getenv("YOUR_API_KEY"))
genai.configure(api_key="YOUR_API_KEY")

### Safety Category
# HARASSMENT (괴롭힘): 성별, 성적지향, 종교, 인종 등 보호받는 개인의 특성에 대해 부정적이거나 해로운 언급을 하는 행위
# HATE SPEECH (증오심 표현): 무례하거나 존중하지 않는 태도 또는 저속한 발언
# SEXUAL EXPLICITY (음란물): 성행위 또는 성적으로 노골적인 내용
# DANGEROUS (위해성): 해로운 행위를 야기하는 내용

### Safety Probability
# NEGLIGIBLE: 내용이 안전하지 않을 가능성이 거의 없음
# LOW: 내용이 안전하지 않을 가능성이 낮음
# MEDIUM: 내용이 안전하지 않을 가능성이 중간
# HIGH: 내용이 안전하지 않을 가능성이 높음

### Set Safety Threshold
# BLOCK_NONE: 차단하지 않음	
# BLOCK_ONLY_HIGH: 안전하지 않은 확률이 “높음”일 경우만 차단	
# BLOCK_MEDIUM_AND_ABOVE: 안전하지 않을 확률이 “중간” 이상일 경우 차단	
# BLOCK_LOW_AND_ABOVE: 안전하지 않을 확률이 “낮음” 이상일 경우 차단	

safety_settings=[
        {
            "category": "HARM_CATEGORY_HARASSMENT",
            "threshold": "BLOCK_NONE",
        },
        {
            "category": "HARM_CATEGORY_HATE_SPEECH",
            "threshold": "BLOCK_NONE",
        },
    ]

model = genai.GenerativeModel('gemini-pro', safety_settings)
response = model.generate_content("나는 니가 싫어")  
#print(response._result)
if response.prompt_feedback.block_reason:
    print(f"사용자 입력에 다음의 문제가 발생하여 응답이 중단되었습니다: {response.prompt_feedback.block_reason.name}")
else:
    print(response.text)