#!/usr/bin/env python3

import aws_cdk as cdk

from a.a_stack import AStack


app = cdk.App()
AStack(app, "a")

app.synth()
