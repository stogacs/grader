from pyston import PystonClient, File


async def getLanguages():
    client = PystonClient()
    runtime = await client.runtimes()
    runtime = [i.language for i in runtime]

    return runtime


async def execute(code, lang, input):
    client = PystonClient()
    out = await client.execute(lang, [File(code)], stdin=input)
    return out.raw_json


async def getOutput(code, lang, input):
    dat = await execute(code, lang, input)
    return dat["run"]["stdout"]
