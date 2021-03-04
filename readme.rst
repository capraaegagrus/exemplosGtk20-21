H1 -- O maior nivel de cabeceira
********************************

H2 -- Axuda proxecto exemplo
============================

H4 -- Subsubsección
+++++++++++++++++++

`Enlaces`_

Foto da nosa vaquiña_.



**Exemplo de uso do linguaxe de marcado rst**

*O texto en cursiva vai cun só simbolo*

Podemos facer listas:
 * Unha cousa
 * Outra cousa

Ou:

 1. Elemento 1
 2. Elemento 2

Tamén:
 - Outra
 - Forma
 - Diferente


Taboa simple:

===== ===== =====
 Entradas   Saida
----------- -----
False False True
True  False True
False False False
===== ===== =====

Táboa complexa:

+---------------+--------------+--------------+
|  Cabeceira1   |  Cabeceira2  |  Cabeceira3  |
+===============+==============+==============+
|    Celda11    |    Celda12   |   Celda13    |
+---------------+--------------+--------------+
|    Celda21    |    Celda22   |   Celda23    |
+---------------+--------------+--------------+
|    Celda31    | Celda        | Celda13      |
+---------------+ expandida    + Unidas       +
|    Celda41    | en liñas     | Celda12      |
+---------------+--------------+--------------+

Enlaces
-------

Deseñado no `Centro de formación profesional Daniel Castelao <https:\\www.danielcastelao.org>`_

.. _vaquiña:
.. figure:: _static/vaquita.jpg
   :align:  center

   A vaca do centro

:download: `Un informe de reportlab <_static/primeiroInforme.pdf>`_

.. |vaca| image:: _static/simboloVaca.jpg

A |vaca| é o icono que está quedando dentro deste do documento como nexo de unión.

.. note::
   Respetar o formato de tabulación para que interprete o texto como parte da nota.

.. warning::
   Esta é un advertencia, coidado!

.. versionadded:: 0.0.0.1

Un exemplo de código::

   def funcion (parametro = True):
      """Exemplo dunha funición
         que non fai moito"""

      return "Adeus"



o código do programa da función tamén podería devoltar ``return "Chao"`` no caso de querer un saúdo menos formal.

Si queremos facer referencia a un módulo :mod:`threading` que está na clase :class:`threading.Thread`.

Un enlace a unha función :func:`time.time`