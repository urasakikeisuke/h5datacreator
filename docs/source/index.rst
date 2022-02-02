===============
H5 Data Creator
===============

依存
====

* Python>=3.6
* Numpy
* h5py==2.10.0

インストール
============

.. code-block:: bash

  pip install git+https://github.com/shikishima-TasakiLab/h5datacreator

サンプル
========

.. code-block:: python

  from h5datacreator import H5Dataset
  import numpy as np
  import cv2

  h5file = H5Dataset(path='sample.hdf5')

  # '/data/0/image'に画像を格納する
  h5data: h5py.Group = h5file.get_next_data_group()
  img: np.ndarray = cv2.imread('sample.png', cv2.IMREAD_ANYCOLOR)
  set_bgr8(
    h5_group=h5data,
    tag='image',
    data=img,
    frame_id='camera'
  )

  # '/intrinsic/camera'にカメラ行列を格納する
  h5intrinsic: h5py.Group = h5file.get_common_group('intrinsic')
  set_intrinsic(
    h5_group=h5intrinsic,
    tag='camera',
    data_fx=128.0, data_fy=128.0,
    data_cx=256.0, data_cy=128.0,
    data_height=256, data_width=128,
    frame_id='camera'
  )

  h5file.close()

使い方
======

.. toctree::
  :maxdepth: 2
  :glob:

  *
