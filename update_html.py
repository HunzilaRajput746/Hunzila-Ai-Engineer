import re

html_path = 'D:/My_projects/portfolio/index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Inject data-project-id into project cards
project_count = 1
def replace_project(match):
    global project_count
    replacement = f'<div class="{match.group(1)}" data-project-id="p{project_count}">'
    project_count += 1
    return replacement

content = re.sub(r'<div class="(project-card[^"]*)">', replace_project, content)

# 2. Add Modal HTML before </body>
modal_html = '''
    <!-- Project Detail Modal -->
    <div id="projectModal" class="project-modal">
        <div class="modal-backdrop"></div>
        <div class="modal-container">
            <button class="modal-close" aria-label="Close Modal"><i class="fas fa-times"></i></button>
            <div class="modal-content">
                <div class="modal-hero">
                    <img id="modalImg" src="" alt="Project Image">
                    <div class="modal-hero-overlay"></div>
                </div>
                <div class="modal-body">
                    <div class="modal-header">
                        <span id="modalLabel" class="project-label vibe-label"></span>
                        <h2 id="modalTitle">Project Title</h2>
                        <div class="project-links">
                            <a id="modalGithub" href="#" target="_blank" class="project-link"><i class="fab fa-github"></i></a>
                            <a id="modalDemo" href="#" target="_blank" class="project-link"><i class="fas fa-external-link-alt"></i></a>
                        </div>
                    </div>
                    
                    <div class="modal-tech" id="modalTech">
                        <!-- Tech spans injected here -->
                    </div>
                    
                    <div class="modal-description" id="modalDesc">
                        <p>Project Description.</p>
                    </div>

                    <div class="modal-workflow">
                        <h3><i class="fas fa-project-diagram"></i> Architecture & Workflow</h3>
                        <div class="workflow-box" id="modalWorkflow">
                            Workflow description goes here...
                        </div>
                    </div>
                    
                    <div class="modal-footer">
                        <p>Developed by <span class="developer-name">Hunzila Nisar</span></p>
                    </div>
                </div>
            </div>
        </div>
    </div>
'''

if 'id="projectModal"' not in content:
    content = content.replace('</body>', modal_html + '\n</body>')

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Updated {project_count - 1} project cards and injected Modal HTML.")
