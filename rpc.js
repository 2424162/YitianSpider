var sig
function encodeMap(str_data){
    Java.perform(function(){
        var KSecurity = Java.use("com.kuaishou.android.security.KSecurity")
        sig = KSecurity.atlasSign(str_data)
    });
    return sig
}
rpc.exports = {
    encode:encodeMap
}