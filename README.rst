This is a `Jupyter notebook <https://jupyter.org/>`_ kernel for communicating with a `MicroPython <https://micropython.org/>`_ enabled
`NodeMCU <https://en.wikipedia.org/wiki/NodeMCU>`_ attached via USB from within a Jupyter notebook.

This work has been directly derived from the ubit_kernel support for the BBC micro:bit 
done by Thomas Kluyver which you can find `here <https://github.com/takluyver/ubit_kernel>`__.

MicroPython is a variant of the Python programming language that runs on such
tiny computers. It's a powerful way to program the NodeMcu. For tutorials
and reference information, see the `MicroPython documentation <https://docs.micropython.org/en/latest/esp8266/index.html>`__.

`Jupyter <http://jupyter.org/>`__ is a set of tools for interactive programming.
This package allows Jupyter interfaces to run MicroPython code directly on the
NodeMcu

Set-up steps:

1. Plug in your NodeMcu and ensure it has MicroPython on it. To do this have a look  
   at `this tutorial <https://docs.micropython.org/en/latest/esp8266/esp8266/tutorial/intro.html#intro>`__,
   and follow the instructions there to flash it onto the NodeMcu.

2. Depending on your system, you may need some extra setup so that the kernel
   can talk to your NodeMcu using a serial port.

   * On Linux, you may need to add yourself to the *dialout* group.
     Run ``sudo usermod -a -G dialout <your-username>``, then log out and in again.
   * On Windows, you need to install a suitable USB to serial driver first.

3. `Install Jupyter <http://jupyter.readthedocs.org/en/latest/install.html>`__.
4. Install this package::

       pip install nodemcu_kernel
       python3 -m nodemcu_kernel.install

When you start the Jupyter Notebook, there should be a *NodeMcu* option in the
menu to create a new notebook.
