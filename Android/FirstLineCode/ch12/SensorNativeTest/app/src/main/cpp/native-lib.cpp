#include <jni.h>
#include <string>

#include <android/sensor.h>
#include <android/log.h>
#include <android/looper.h>

#define TAG "SENSOR_NATIVE"
#define LOGI(...) __android_log_print(ANDROID_LOG_INFO, TAG, __VA_ARGS__)
#define LOGD(...) __android_log_print(ANDROID_LOG_DEBUG, TAG, __VA_ARGS__)

#define LOOPER_ID 1
#define SAMP_PER_SEC 100 //i've changed to 120, even 10, but nothing happen


extern "C" JNIEXPORT jstring JNICALL
Java_com_example_sensornativetest_MainActivity_stringFromJNI(
        JNIEnv *env,
        jobject /* this */) {
    std::string hello = "Hello from C++";
    return env->NewStringUTF(hello.c_str());
}


extern "C" JNIEXPORT jstring JNICALL
Java_com_example_sensornativetest_MainActivity_startMonitoring(JNIEnv* env, jobject /* this */) {
    ASensorManager* sensorManager = ASensorManager_getInstance();

    // Returns the looper associated with the calling thread, or NULL if there is not one.
    ALooper* looper = ALooper_forThread();
    if(looper == NULL)
        looper = ALooper_prepare(ALOOPER_PREPARE_ALLOW_NON_CALLBACKS);

    ASensorRef accelerometerSensor = ASensorManager_getDefaultSensor(sensorManager,ASENSOR_TYPE_ACCELEROMETER);
    LOGI("accelerometerSensor: %s, vendor: %s", ASensor_getName(accelerometerSensor), ASensor_getVendor(accelerometerSensor));

    ASensorEventQueue* queue = ASensorManager_createEventQueue(sensorManager, looper, LOOPER_ID, NULL, NULL);

    ASensorEventQueue_enableSensor(queue, accelerometerSensor);
    ASensorEventQueue_setEventRate(queue, accelerometerSensor, (1000L/SAMP_PER_SEC)*1000);

    int ident;//identifier
    int events;
    while (1) {
        while ((ident=ALooper_pollAll(-1, NULL, &events, NULL) >= 0)) {
            // If a sensor has data, process it now.
            if (ident == LOOPER_ID) {
                ASensorEvent event;
                while (ASensorEventQueue_getEvents(queue, &event, 1) > 0) {
                    LOGI("accelerometer X = %f y = %f z=%f ", event.acceleration.x, event.acceleration.y, event.acceleration.z);
                }
            }
        }
    }
    return env->NewStringUTF("");
}