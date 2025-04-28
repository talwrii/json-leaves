# json-leaves
**@readwithai** - [X](https://x.com/readwithai) - [blog](https://readwithai.substack.com/) - [machine-aided reading](https://www.reddit.com/r/machineAidedReading/) - [📖](https://readwithai.substack.com/p/what-is-reading-broadly-defined
)[⚡️](https://readwithai.substack.com/s/technical-miscellany)[🖋️](https://readwithai.substack.com/p/note-taking-with-obsidian-much-of)

Turn a JSON object into path-value pairs suitable for grepping.

JSON is quite nice but digging through JSON can be a pain - as can building queries to fetch the values you have found. `json-leaves` allows you to use grep and other command-line tools to find what you want and then gives you a selector (suitable for use in other tools like `python` or `jq` so that you can programmatically do the same thing).

# Alternatives and prior work
I could not quickly find a command-line tool to the same thing. I found a [recipe  for jq](https://github.com/jqlang/jq/issues/78) but this sufficiently unwieldy that I do not want to use it - though it could be placed in a script that you place on your path. I wanted to make something reusable on any machine.

More generally, any use of this tools likely wants to be aware of the `jq` tool which provides a DSL to perform many JSON operations from the command-line.

This tool is somewhat related to [GenSON](https://github.com/wolverdude/genson/) which will return the schema of JSON data in that it helps you understand unknown JSON data. The author wrote [short-schema](https://github.com/talwrii/short_schema?tab=readme-ov-file) some years ago which renders the output from GenSON easily readable.

Those who are incapable of using the command-line and used to spending their lives clicking because they are too lazy to learn anything, may well use JSON browsers such as those in VSCode or browsers. Or you may simply prefer these tools.

# Installation
You can install `json-leaves` using [pipx](https://github.com/pypa/pipx):
```
pipx install json-leaves
```

# Usage
This fetches data related to the pip installations of the kitty-plotnine package and then unpacks all leaves and values.
```
curl https://pypistats.org/api/packages/kitty-plotnine/python_major | json-leaves
```

If you want to show just the values you can use:

curl https://pypistats.org/api/packages/kitty-plotnine/python_major | json-leaves

To distinguish between strings and integers (or `null`s) `--quote` (or `-q`).
```
curl https://pypistats.org/api/packages/kitty-plotnine/python_major | json-leaves -q
```

You can also output JSON data with `--json` and include nodes as well as leaves with `--nodes`


## About me
I am **@readwithai**. I create tools for reading, research and agency sometimes using the markdown editor [Obsidian](https://readwithai.substack.com/p/what-exactly-is-obsidian).

I also create a [stream of tools](https://readwithai.substack.com/p/my-productivity-tools) that are related to carrying out my work.

I write about lots of things - including tools like this - on [X](https://x.com/readwithai).
My [blog](https://readwithai.substack.com/) is more about reading and research and agency.

![@readwithai logo](./logo.png)
