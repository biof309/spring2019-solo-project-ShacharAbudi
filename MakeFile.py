slides: JupyterLab_HPS.ipynb
   jupyter nbconvert JupyterLab_HPS.ipynb --to slides --reveal-prefix="https://revealjs.com"
   mv JupyterLab_HPS.slides.html JupyterLab_HPS.html

init: .git/

.git/:
   curl --user 'ShacharAbudi' https://api.github.com/user/repos --data '{"name":"HPS_Project","description":"A presentation about HPS."}'
   git init
   git add --all
   git commit --message "First commit"
   git remote add origin https://github.com/ShacharAbudi/HPS_Project.git
   git push --set-upstream origin master
