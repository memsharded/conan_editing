import os
import shutil
from contextlib import contextmanager


os.system("conan remove * -f")
os.system("cd hello && conan export memsharded/testing")
os.system("cd chat && conan export memsharded/testing")
os.system("cd social && conan test_package --build")

def replace_file(filepath, text, new_text):
    with open(filepath, "r") as handle:
        content = handle.read()
    content = content.replace(text, new_text)
    with open(filepath, "w") as handle:
        handle.write(content)

@contextmanager
def chdir(newdir):
    old_path = os.getcwd()
    os.chdir(newdir)
    try:
        yield
    finally:
        os.chdir(old_path)


def open_project(project_name):
    # local edition
    build_folder = "%s_build" % project_name
    try:
        shutil.rmtree(build_folder)
    except:
        pass
    os.makedirs(build_folder)
    with chdir(build_folder):
        os.system("conan install ../%s -g txt" % project_name)
        os.system("conan build ../%s" % project_name)
        os.makedirs("package")

def build_project(project_name):
    with chdir("%s_build" % project_name):
        os.system("conan build ../%s" % project_name)

def package_project(project_name, package):
    with chdir("%s_build" % project_name):
        os.system("cd package && conan package ../../%s --build_folder=.." % project_name)
        os.system("cd package && conan package_files %s -f" % package)

open_project("chat")
replace_file("chat/src/chat.cpp", "Chat", "NewChat")
build_project("chat")
package_project("chat", "Chat/0.1@memsharded/testing")
open_project("social")
build_project("social")
replace_file("chat/src/chat.cpp", "NewChat", "Chat")


"""os.system("cd social && conan test_package --build=missing")
replace_file("chat/src/chat.cpp", "NewChat", "HipsterChat")
package_project("chat", "Chat/0.1@memsharded/testing")
os.system("cd social && conan test_package --build=missing")
replace_file("chat/src/chat.cpp", "HipsterChat", "Chat")"""