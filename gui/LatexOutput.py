#!/usr/bin/env python

import sys
import subprocess
import os
import os.path
import shutil

from backend.utils import resource, multiple_replace

def LatexString(char):
    latexChar = open(resource('resources','char.tex')).read()
    latexChar = multiple_replace({'PYCHARGEN_STATS_OVERVIEW':_statsString(char),
                                  'PYCHARGEN_COMMON_SKILLS_OVERVIEW':_skillOverviewString(char),
                                  'PYCHARGEN_RESISTANCES_OVERVIEW':_resistanceString(char),
                                  'PYCHARGEN_SKILL_FULLLIST':_skillFullListString(char),
                                  'PYCHARGEN_CHARACTER_NAME':char.GetMisc('Name'),
                                  'PYCHARGEN_LEVEL':str(char.GetMisc('Level')),
                                  'PYCHARGEN_PROFESSION':char.GetMisc('Profession'),
                                  },latexChar)
    return latexChar

def SaveLatexFile(char,filename):
    with open(filename,'w') as f:
        f.write(LatexString(char))

def FindExecutable():
    """Attempts to find the latex executable"""
    if sys.platform=='win32':
        #executable = resource('resources','pdflatex.exe')
        executable = resource('resources','texlive-small','bin','win32','pdflatex.exe')
        if executable is None:
            raise EnvironmentError("""Could not find resources\pdflatex.exe""")
    else:
        executable = 'pdflatex'
        with open(os.devnull,'w') as devnull:
            if subprocess.call(['which',executable],stdout=devnull,stdin=devnull):
                raise EnvironmentError("""Could not find pdflatex.  Please install using 'sudo apt-get texlive-latex-base'""")
    return executable

def WorkingDir():
    """
    Finds the appropriate working directory for temporary files.
    Makes it in the resources directory if not existing.
    """
    folderName = 'latex_workingdir'
    workingDir = resource('resources',folderName)
    if workingDir is not None:
        return workingDir
    workingDir = os.path.join(resource('resources'),
                              folderName)
    os.makedirs(workingDir)
    return workingDir

def _escape(inString):
    return multiple_replace({'_':'\\_',
                             '^':'\\textasciicircum{}',
                             '{':'\\{',
                             '}':'\\}',
                             '%':'\\%',
                             '\\':'\\textbackslash{}',
                             '&':'\\&',
                             '~':'\\textasciitilde{}'},
                            inString)

def CompileLatex(char,filename):
    outputdir = os.path.dirname(filename)
    workingdir = WorkingDir()
    jobname = os.path.splitext(os.path.basename(filename))[0]
    outputfile = os.path.join(outputdir,jobname+'.pdf')
    SaveLatexFile(char,os.path.join(workingdir,jobname+'.tex'))
    executable = FindExecutable()
    #Two passes, since latex uses temporary files strangely.
    for i in range(2):
        args = [executable,
                '-interaction=nonstopmode', '-recorder',
                jobname+'.tex']
        subprocess.call(args,cwd=workingdir)
    shutil.move(os.path.join(workingdir,jobname+'.pdf'),
                os.path.join(outputdir))




def _statsString(char):
    return '\n'.join('\\Stat{{{name}}}{{{value}}}{{{bonus}}}'.format(
                                  name=_escape(st.Name),
                                  value=_escape(str(st.Value)),
                                  bonus=_escape(str(st.Bonus())))
                     for st in char.Stats)

def _skillOverviewString(char):
    return '\n'.join('\\CommonSkill{{{name}}}{{{ranks}}}{{{bonus}}}'.format(
                                  name=_escape(sk.Name),
                                  ranks=_escape(str(sk.Value)),
                                  bonus=_escape(str(sk.Bonus())))
                     for sk in char.Skills if sk.CommonlyUsed)

def _resistanceString(char):
    return '\n'.join('\\Resistance{{{name}}}{{{bonus}}}'.format(
                                  name=_escape(res.Name),
                                  bonus=_escape(str(res.Bonus())))
                     for res in char.Resistances)

def _skillFullListString(char):
    return '\n'.join('\\DetailSkill{{{name}}}{{{ranks}}}{{{bonus}}}{{{depth}}}'.format(
                                  name=_escape(sk.Name),
                                  ranks=_escape(str(sk.Value)),
                                  bonus=_escape(str(sk.Bonus())),
                                  depth=_escape(str(sk.Depth)))
                     for sk in char.Skills)
