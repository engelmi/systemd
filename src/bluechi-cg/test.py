#!/usr/bin/python3
# SPDX-License-Identifier: MIT-0

from dasbus.loop import EventLoop
import dasbus.connection


bus = dasbus.connection.SystemMessageBus()


def test(cgtop):
    print("\033[2J")
    print("\033[0;0H")
    print(f'{"ControlGroup":<35} | {"Tasks":<6} | {"%CPU":<10} | {"Memory":<10} | {"Input/s":<10} | {"Output/s":<10} |')
    print('-'*98)
    for cg in cgtop:
        name, task_count, cpu, memory, io_input, io_output = cg
        print(f'{str(name)[:35]:<35} | {str(task_count)[:6]:<6} | {str(cpu)[:10]:<10} | {str(memory)[:10]:<10} | {str(io_input)[:10]:<10} | {str(io_output)[:10]:<10} |')


proxy = bus.get_proxy("org.eclipse.bluechi",
                      "/org/eclipse/bluechi", interface_name="org.eclipse.bluechi")
proxy.CGTop.connect(test)

loop = EventLoop()
loop.run()
