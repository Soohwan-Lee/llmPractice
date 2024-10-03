from pathlib import Path
from openai import OpenAI
import os

# Initialize OpenAI client with API key (please replace "YOUR_API_KEY" with your actual key)
client = OpenAI(api_key="YOUR_API_KEY")

# Bullet points content
contents = [
    "Hello, I am Soohwan from UNIST. Today, I will present our research on expanding the design space of computer vision-based interactive systems for group dance practice.",
    "Let's start by looking at synchronized group dance, particularly dance cheerleading. Practice this kind of dance is difficult, because it requires high levels of synchronization, often without professional trainers, making it difficult for novices to receive consistent and accurate feedback on their performance in a group context.",
    "Currently, most dance practice systems are designed for individual use. There are fewer resources for group contexts. Our research aims to fill this gap by exploring how to support group dance practice using computer vision technology, specifically with a single RGB camera.",
    "Our main question is: What is the design space for group dance practice? We're focusing on synchronized group dance, using computer vision, for amateur dancers, and exploring different types of feedback.",
    "Our research had four main phases. First, we reviewed existing literature. Then, we did a formative study to understand user needs. Next, we had an ideation phase to come up with new design ideas. Finally, we validated these ideas with potential users.",
    "In the first phase, we looked at existing dance practice systems to understand what's already been done.",
    "We began our research by examining the existing design space of interactive systems for dance practice. Our starting point was the Dance Interactive Learning System Workflow by Raheb et al., which outlines four key elements: student moving, capturing movement, processing data, and feedback.",
    "Based on these 4 elements, we analyzed 19 concepts from Raheb et al.'s review and added 5 more vision-based concepts from 2019-2024. This comprehensive review helped us identify current design dimensions and potential gaps in group dance support.",
    "In the second phase, we conducted a formative study to understand user needs and pain points in real group dance practice contexts.",
    "We observed UNIST Cheerleading Crew's practice sessions over three weeks and conducted in-depth interviews with 16 participants. We focused on small-group practice scenarios.",
    "We found that practice often happens in small groups. Instructors can't always help everyone, so dancers struggle to know when and how to correct their movements. So we narrow-down our research scope to small-group practice.",
    "We also learned about different types of feedback used in practice. We identified differences between real-time feedback during movement and post-feedback after movement.",
    "From our observations and interviews, we categorized 24 insights into real-time feedback, post feedback, and common insights. These formed the basis for our next phase.",
    "In the third phase, we held a design ideation workshop to generate new concepts for interactive systems supporting group dance practice.",
    "We conducted a Design Ideation Workshop to generate innovative ideas for small group dance practice feedback. The workshop, involving 6 researchers over 2 hours, progressed from introducing 24 user insights to brainstorming, resulting in 55 seed ideas that were refined into 15 storyboards.",
    "Refined 15 storyboards represented different ways that computer vision could be used to support group dance practice. Refining criteria were to represent group contexts or anticipate member interactions.",
    "Our expanded design space includes new dimensions like feedback privacy and timing. These add to the existing dimensions we found in current dance systems.",
    "In the final phase, we evaluated our expanded design space through technology probe and speed dating workshops.",
    "We conducted three sessions, each with three participants. The technology probe workshop familiarized participants with vision-based systems, while the speed dating workshop assessed the practicality of our design concepts.",
    "For this workshop, we utilize 5 technology probes with augmented mirror from storyboards and 15 storyboards from Phase 3 ideation.",
    "After technology probe workshop, First, Participants anticipated objective AI ratings and detailed movement tracking. For instance, one participant mentioned expecting the system to provide an objective assessment when instructors might disagree. Second, Participants were curious about the system's capabilities. They wanted to understand how it measured similarity between dancers and what it considered as similar movements. Third, Users identified limitations of the vision system. A key issue was occlusion - when dancers are close together, their bodies might overlap in the camera view. Additionally, participants compared the system to karaoke machines, they felt it couldn't fully replace human assessment of dance movements. Finally, Participants proposed ideas for improvement. They suggested making the system more sensitive for basic movements and using it to demonstrate body mechanics rather than just for assessment.",
    "The speed dating workshop provided insights into three main areas: First, about Feedback timing: Participants noted that well-timed feedback, such as guidance just before a difficult section, could increase focus and tension in a beneficial way. Second, group reflection, there was passion for features that promote cooperation, such as using sound to help dancers match their movements. Lastly, Public vs Private feedback: Interestingly, some participants preferred public feedback, suggesting it allows for collective learning and pointing out errors together.",
    "Also they discuss about challenge and opportunity about interactive systems. About challenge, Quantified evaluations raised concerns. Some participants questioned the necessity of scores. This highlights the need to carefully consider how performance is quantified and presented. Also, about instructor’s role, this underscores the importance of integrating these systems with existing teaching methods. On the other hands, Opportunities, Participants saw potential for using the system in various ways, such as for final evaluations after group practice or as a fun, such as competitive game. They also stressed the importance of adapting the system for different learning stages.",
    "We found a clear preference for different types of feedback at different stages of practice. During movements, dancers prefer short, auditory feedback. After practice, they want more detailed, visual feedback. Also, It's crucial to consider the group's cultural and organizational attributes when designing feedback systems. Some groups may be more comfortable with public feedback than others. We also stress the need for adaptive feedback systems that can provide to different learning stages and dance styles.",
    "We identified several technical challenges with RGB cameras, such as occlusion issues when dancers overlap and limited depth perception. These need to be addressed for effective group dance tracking. User reactions to feedback mechanisms varied, with some preferring guidance just before difficult movements. We also noted an interesting shift in preferences from private to public feedback as dancers recognized the benefits of collective learning. This highlights the importance of designing systems that can support both individual improvement and group cohesion.",
    "In expanding and evaluating the design space, we focused on how feedback can influence group dynamics. We explored three key areas: First, we examined perceptions of quantitative score-based feedback. As one participant noted, the goal should be improvement, not competition. Second, we observed a shift in preferences from private to public feedback. Participants recognized the value of collective learning, with one stating that group feedback allows for shared understanding of mistakes. Lastly, we emphasized the importance of systems promoting group reflection and cooperation. One design concept using sound-based feedback was praised for encouraging synchronization and fostering a sense of teamwork. These insights highlight the complex role of feedback in group dance practice and the need for carefully designed interactive systems.",
    "Based on our findings, we propose several key design implications: For Alternative Technologies, There's a clear need to explore technologies beyond basic RGB cameras to overcome current limitations in tracking multiple dancers simultaneously. And perspective of Anonymity and Group Reflection, Systems like ZoombaTogether (2023) demonstrate the potential of anonymous, collective feedback in group settings. This approach could maintain a supportive environment while still providing personalized insights. Balancing Individual and Group Needs: Future systems should strive to support both individual improvement and group cohesion, perhaps by offering both private and public feedback options.",
    "We stress the importance of developing systems that can adapt to different dance learning context.",
    "The Adapt2Learn system serves as an example of how technology can be tailored to various learning contexts. In the perspective of Integration with Existing Practices, It's crucial to design systems that complement rather than replace traditional instruction methods, addressing concerns about potential conflicts between AI feedback and human instructors.",
    "To conclude, our work expands the design space for interactive group dance practice systems. We've identified new design dimensions and challenges specific to group contexts, providing a foundation for future research and development in this area.",
    "Thank you for your attention. This study has a lot of steps, so please check out the paper for more details. If you have any questions feel free to ask me! Thank you!"
]

# Ensure directory for audio files exists
output_dir = Path("./LLMs/GPT/")
output_dir.mkdir(parents=True, exist_ok=True)

# Loop over the content and create MP3 files in sequence
for i, text in enumerate(contents, 1):
    speech_file_path = output_dir / f"{i}.mp3"
    
    response = client.audio.speech.create(
        model="tts-1",
        voice="onyx",
        input=text
    )
    
    response.stream_to_file(speech_file_path)

print("MP3 files generated successfully.")
