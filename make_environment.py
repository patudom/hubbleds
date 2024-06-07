from os.path import dirname, join, realpath
import subprocess
from yaml import dump, load, CLoader

filename = "environment.yml"
dirpath = dirname(realpath(__file__))
filepath = join(dirpath, filename)

ps = subprocess.run(["conda", "env", "export"], capture_output=True)
env = load(ps.stdout, Loader=CLoader)
env.pop("prefix")
env.pop("name")

def pip_filter(d):
    return isinstance(d, dict) and "pip" in d

def dep_filter(d):
    return pip_filter(d) or \
           (isinstance(d, str) and d.startswith("pip=")) 

env["dependencies"] = [d for d in env["dependencies"] if dep_filter(d)]

git_repos = {
    "cosmicds": "https://github.com/cosmicds/cosmicds.git",
    "ipywwt": "https://github.com/nmearl/ipywwt.git",
}
pip_installs = next(filter(pip_filter, env["dependencies"]))
deps = [dep for dep in pip_installs["pip"] if not any(dep.startswith(f"{repo}=") for repo in git_repos)]
deps = [dep for dep in deps if not dep.startswith("hubbleds=")]
deps.extend(f"git+{url}" for url in git_repos.values())
pip_installs["pip"] = deps

with open(filepath, 'w') as f:
    dump(env, f)
