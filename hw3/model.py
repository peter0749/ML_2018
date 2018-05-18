import tensorflow as tf
from tensorflow.contrib.slim.nets import vgg
slim = tf.contrib.slim

def VGG16(inputs, n_classes, freeze=False):
    trainable = not freeze
    
    inputs = tf.cast(inputs, tf.float32)
    inputs = (inputs-127.5) / 127.5 # rescale: 0~255 -> -1~+1
    
    with tf.variable_scope("vgg_16"):
        with slim.arg_scope(vgg.vgg_arg_scope()):
            net = slim.repeat(inputs, 2, slim.conv2d, 64, [3, 3], scope='conv1', trainable=trainable)
            net = slim.max_pool2d(net, [2, 2], scope='pool1')
            net = slim.repeat(net, 2, slim.conv2d, 128, [3, 3], scope='conv2', trainable=trainable)
            net = slim.max_pool2d(net, [2, 2], scope='pool2')
            net = slim.repeat(net, 3, slim.conv2d, 256, [3, 3], scope='conv3', trainable=trainable)
            net = slim.max_pool2d(net, [2, 2], scope='pool3')
            net = slim.repeat(net, 3, slim.conv2d, 512, [3, 3], scope='conv4', trainable=trainable)
            net = slim.max_pool2d(net, [2, 2], scope='pool4')
            net = slim.repeat(net, 3, slim.conv2d, 512, [3, 3], scope='conv5', trainable=trainable)
            net = slim.max_pool2d(net, [2, 2], scope='pool5')
    #Append fully connected layer
    net = slim.flatten(net)
    """
    net = slim.fully_connected(net, 256,
            weights_initializer=tf.contrib.layers.xavier_initializer(),
            weights_regularizer=slim.l2_regularizer(0.0005),
            scope='finetune/fc1')
    """
    net = slim.fully_connected(net, n_classes,
            activation_fn=None,
            weights_initializer=tf.contrib.layers.xavier_initializer(),
            weights_regularizer=slim.l2_regularizer(0.001), # strong regularization
            scope='finetune/classification')
    return net
