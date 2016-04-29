import invoke
import livereload
import shutil

server = livereload.Server()


@invoke.task
def clean():
    shutil.rmtree('./build')


@invoke.task(pre=[clean])
def build():
    invoke.run('sphinx-build ./docs ./build', pty=True)


@invoke.task(pre=[build])
def serve():
    server.watch('./_static/**/*', build);
    server.watch('./_templates/**/*', build);
    server.watch('./docs/**/*', build);
    server.watch('./granite/**/*', build);
    server.serve(
        root='./build',
        host='localhost',
        liveport=35729,
        port=8080
    )
