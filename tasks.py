import invoke
import livereload
import os
import shutil

server = livereload.Server()

def dir(path):
    return os.path.abspath(os.path.join(os.getcwd(), path))

@invoke.task
def clean():
    shutil.rmtree('./build')


@invoke.task(pre=[clean])
def build():
    invoke.run('sphinx-build ./docs ./build', pty=True)


@invoke.task(pre=[build])
def serve():
    server.watch(dir('./docs/'), build)
    server.watch(dir('./granite/'), build)
    server.watch(dir('../sphinx-granite/'), build)

    server.serve(
        root='./build',
        host='localhost',
        liveport=35729,
        port=8080
    )
