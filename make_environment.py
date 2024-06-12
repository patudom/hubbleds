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


keep_deps = ["pip", "python"]
def pip_filter(d):
    return isinstance(d, dict) and "pip" in d

def dep_filter(d):
    return pip_filter(d) or \
           (isinstance(d, str) and any(d.startswith(f"{dep}=") for dep in keep_deps))

env["dependencies"] = [d for d in env["dependencies"] if dep_filter(d)]

# We only want to keep the major.minor.patch version for Python and pip
for keep in keep_deps:
    idx, dep = next((i, d) for i, d in enumerate(env["dependencies"]) if d.startswith(keep))
    dep_split = dep.split("=")
    if len(dep_split) > 2:
        dep = "=".join(dep_split[:2])
    env["dependencies"][idx] = dep

git_repos = {
    "ipywwt": "https://github.com/nmearl/ipywwt.git",
}
want_dev_install = ["hubbleds", "cosmicds"]
pip_installs = next(filter(pip_filter, env["dependencies"]))
deps = [dep for dep in pip_installs["pip"] if not any(dep.startswith(f"{repo}=") for repo in git_repos)]
deps = [dep for dep in deps if not any(dep.startswith(f"{p}=") for p in want_dev_install)]
deps.extend(f"git+{url}" for url in git_repos.values())
pip_installs["pip"] = deps

with open(filepath, 'w') as f:
    dump(env, f)
