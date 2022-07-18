#!/usr/bin/env python
# coding: utf-8

import subprocess

# procon-gaardenerを呼び、atcoderからacとなったコードを取得する
stdout = subprocess.run(['procon-gardener', 'archive'], shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT).stdout
print(stdout.decode())

# 実行した際に新たにacとなったコードがあるかどうか判別する
if "Archiving 0 code..." in stdout.decode():
    add_cnt = 0

if add_cnt == 0:
    # 何も追加していなければGitにアクセスしない
    print("No added submissions, end process")
else:
    # GitHubにプッシュ
    import git
    import datetime

    dt_now = datetime.datetime.now()
    repo_url = "https://github.com/yus3554/atcoder.git"
    repo = git.Repo()
    repo.git.add("submissions/*")
    repo.git.commit("submissions/*", message="add submission: " + dt_now.strftime('%Y/%m/%d %H:%M:%S'))
    repo.git.push("origin", "main")

    print(f"Finished process, added {add_cnt} files")
