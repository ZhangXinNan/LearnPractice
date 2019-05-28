#include <jni.h>
#include <string>
#include <android/sensor.h>
#include <android/looper.h>
#include <android/log.h>
//#include <android/looper.h>
#include <time.h>
#define LOGI(...) ((void)__android_log_print(ANDROID_LOG_INFO, "TestJNIActivity", __VA_ARGS__))
//#define LOOPER_ID 1
//#define SAMP_PER_SEC 100

ASensorEventQueue* sensorEventQueue;

int accCounter = 0;
int64_t lastAccTime = 0;

int gyroCounter = 0;
int64_t lastGyroTime = 0;

int magCounter = 0;
int64_t lastMagTime = 0;

static int get_sensor_events(int fd, int events, void* data);

struct tm* start;
struct tm* finish;



extern "C" JNIEXPORT jstring JNICALL
Java_com_example_sensorcpptest_MainActivity_stringFromJNI(
        JNIEnv *env,
        jobject /* this */) {

    std::string hello = "Hello from C++";
    return env->NewStringUTF(hello.c_str());
}



extern "C" JNIEXPORT jstring JNICALL
Java_com_example_sensorcpptest_MainActivity_sensorValue( JNIEnv* env, jobject thiz ) {

    ASensorEvent event;
    int events, ident;
    ASensorManager* sensorManager;
    const ASensor* accSensor;
    const ASensor* gyroSensor;
    const ASensor* magSensor;
    void* sensor_data = malloc(1000);

    LOGI("sensorValue() - ALooper_forThread()");

    ALooper* looper = ALooper_forThread();

    if(looper == NULL)
    {
        looper = ALooper_prepare(ALOOPER_PREPARE_ALLOW_NON_CALLBACKS);
    }

    sensorManager = ASensorManager_getInstance();

    accSensor = ASensorManager_getDefaultSensor(sensorManager, ASENSOR_TYPE_ACCELEROMETER);
    gyroSensor = ASensorManager_getDefaultSensor(sensorManager, ASENSOR_TYPE_GYROSCOPE);
    magSensor = ASensorManager_getDefaultSensor(sensorManager, ASENSOR_TYPE_MAGNETIC_FIELD);



    sensorEventQueue = ASensorManager_createEventQueue(sensorManager, looper, 3, get_sensor_events, sensor_data);

    ASensorEventQueue_enableSensor(sensorEventQueue, accSensor);
    ASensorEventQueue_enableSensor(sensorEventQueue, gyroSensor);
    ASensorEventQueue_enableSensor(sensorEventQueue, magSensor);

    //Sampling rate: 100Hz
    int a = ASensor_getMinDelay(accSensor);
    int b = ASensor_getMinDelay(gyroSensor);
    int c = ASensor_getMinDelay(magSensor);
    LOGI("min-delay: %d, %d, %d",a,b,c);
    ASensorEventQueue_setEventRate(sensorEventQueue, accSensor, 100000);
    ASensorEventQueue_setEventRate(sensorEventQueue, gyroSensor, 100000);
    ASensorEventQueue_setEventRate(sensorEventQueue, magSensor, 100000);

    LOGI("sensorValue() - START");
    std::string hello = "Hello from C++";
    return env->NewStringUTF(hello.c_str());
}



static int get_sensor_events(int fd, int events, void* data) {
    ASensorEvent event;
    //ASensorEventQueue* sensorEventQueue;
    while (ASensorEventQueue_getEvents(sensorEventQueue, &event, 1) > 0) {
        if(event.type == ASENSOR_TYPE_ACCELEROMETER) {
            LOGI("accl(x,y,z,t): %f %f %f %lld", event.acceleration.x, event.acceleration.y, event.acceleration.z, event.timestamp);
            if(accCounter == 0 || accCounter == 1000)
            {
                LOGI("Acc-Time: %lld (%f)", event.timestamp,((double)(event.timestamp-lastAccTime))/1000000000.0);
                lastAccTime = event.timestamp;
                accCounter = 0;
            }

            accCounter++;
        }
        else if(event.type == ASENSOR_TYPE_GYROSCOPE) {
            LOGI("gyro(x,y,z,t): %f %f %f %lld", event.acceleration.x, event.acceleration.y, event.acceleration.z, event.timestamp);
            if(gyroCounter == 0 || gyroCounter == 1000)
            {

                LOGI("Gyro-Time: %lld (%f)", event.timestamp,((double)(event.timestamp-lastGyroTime))/1000000000.0);
                lastGyroTime = event.timestamp;
                gyroCounter = 0;
            }

            gyroCounter++;
        }
        else if(event.type == ASENSOR_TYPE_MAGNETIC_FIELD) {
            LOGI("magn(x,y,z,t): %f %f %f %lld", event.acceleration.x, event.acceleration.y, event.acceleration.z, event.timestamp);
            if(magCounter == 0 || magCounter == 1000)
            {
                LOGI("Mag-Time: %lld (%f)", event.timestamp,((double)(event.timestamp-lastMagTime))/1000000000.0);
                lastMagTime = event.timestamp;
                magCounter = 0;
            }

            magCounter++;
        }

    }
    //should return 1 to continue receiving callbacks, or 0 to unregister
    return 1;
}